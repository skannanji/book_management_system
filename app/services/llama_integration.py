from transformers import AutoTokenizer, AutoModelForCausalLM

class Llama3Integration:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-chat-hf")
        self.model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-chat-hf")

    def generate_summary(self, content):
        inputs = self.tokenizer(f"Summarize the following book content: {content}", return_tensors="pt")
        outputs = self.model.generate(**inputs, max_length=150)
        summary = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return summary

llama_model = Llama3Integration()
