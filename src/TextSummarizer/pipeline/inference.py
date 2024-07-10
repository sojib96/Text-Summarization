from src.TextSummarizer.config.configuration import ConfigurationManager
from transformers import pipeline


class InferencePipeline:
    def __init__(self) -> None:
        self.config = ConfigurationManager().get_model_evaluation_config()

    def prediction(self, input_text):
        tokenizer = self.config.tokenizer_path
        model = self.config.model_path
        gen_kwargs = {"length_penalty": 0.8, "num_beams": 8, "max_length": 128}

        pipeline_object = pipeline("summarization", model=model, tokenizer=tokenizer)

        print("Dialogue:")
        print(input_text)

        output = pipeline_object(input_text, **gen_kwargs)[0]["summary_text"]
        print("\nModel Summary:")
        print(output)

        return output