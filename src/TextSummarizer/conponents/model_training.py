from transformers import TrainingArguments, Trainer
from transformers import DataCollatorForSeq2Seq
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from datasets import load_dataset, load_from_disk
from src.TextSummarizer.entity.config_entity import ModelTrainerConfig
import torch
import os
import sys
from src.TextSummarizer.logging.logger import logging
from src.TextSummarizer.exception.exception import CustomException


class ModelTraining:
    def __init__(self, config: ModelTrainerConfig) -> None:
        self.config = config

    def training_pipeline(self):
        try:
            device = "cuda" if torch.cuda.is_available() else "cpu"
            logging.info(f"Torch {device} version is on!")
            tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckeckpoint)
            logging.info(f"Tokenizer loading completed")
            model = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckeckpoint).to(device)
            logging.info(f"Model loading completed")
            data_collector = DataCollatorForSeq2Seq(tokenizer=tokenizer,model=model)

            dataset_samsum_pt = load_from_disk(self.config.train_data_path)
            logging.info(f"Data loading completed")

            trainer_args = TrainingArguments(
                output_dir=self.config.root_folder, num_train_epochs=self.config.num_train_epochs, warmup_steps=self.config.warmup_steps,
                per_device_train_batch_size=self.config.per_device_train_batch_size, per_device_eval_batch_size=self.config.per_device_train_batch_size,
                weight_decay=self.config.weight_decay, logging_steps=self.config.logging_steps,
                evaluation_strategy=self.config.evaluation_strategy, eval_steps=self.config.eval_steps, save_steps=1e6,
                gradient_accumulation_steps=self.config.gradient_accumulation_steps
            )

            trainer = Trainer(model=model, args=trainer_args,
                    tokenizer=tokenizer, data_collator=data_collector,
                    train_dataset=dataset_samsum_pt["train"], 
                    eval_dataset=dataset_samsum_pt["validation"])
            logging.info(f"Training will start now.")
            trainer.train()
            logging.info(f"Training is completed.")
            ## Save model
            model.save_pretrained(os.path.join(self.config.root_folder,"pegasus-samsum-model"))
            ## Save tokenizer
            tokenizer.save_pretrained(os.path.join(self.config.root_folder,"tokenizer"))
            logging.info(f"model_and_tokenizer is saved to device")

        except Exception as e:
            raise CustomException(e,sys)