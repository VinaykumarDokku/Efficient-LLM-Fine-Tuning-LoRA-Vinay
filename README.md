# 🚀 Fine-Tuning GPT-2 / T5 with Hugging Face Transformers + Streamlit UI

This project demonstrates how to fine-tune a Seq2Seq language model using **LoRA (Low-Rank Adaptation)** on instruction-based datasets with Hugging Face Transformers. It includes:

- ✅ Fine-tuning code with `peft` (for LoRA)
- ✅ Streamlit-based inference UI
- ✅ Hugging Face Hub integration
- ✅ Instruction tuning using `instruction_dataset.json`
- ✅ No-code fine-tuning experiment with Hugging Face AutoTrain

---

##  Fine-Tuning Concepts Covered

| Method                                                | Description                                                                                    |
| ----------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| **Supervised Fine-Tuning (SFT)**                      | Trained on labeled dataset with instruction → input → output structure.                        |
| **Generic/Unsupervised Fine-Tuning**                  | Uses raw `.txt` or `.jsonl` data (not in this project).                                        |
| **Reinforcement Learning with Human Feedback (RLHF)** | Aligns models to preferred human responses via reward modeling (not applied here).             |
| **Direct Preference Optimization (DPO)**              | Trains on (prompt, preferred, rejected) triplets to optimize behavior without reward modeling. |
| **LoRA (Low-Rank Adaptation)**                        | Efficient fine-tuning technique by adding small trainable weights. Applied in this repo.       |

In this project, we apply **Supervised Fine-Tuning** using LoRA on a small instruction dataset and deploy it using Streamlit.

---

##  Project Structure

.
├── inference.py # Streamlit UI for model inference
├── finetuning.py # LoRA-based fine-tuning script
├── utils.py # Custom dataset loading and preprocessing
├── instruction_dataset.json # Labeled dataset with instruction/input/output
├── final_model_lora/ # Output directory for fine-tuned model
└── README.md # Project documentation

markdown
Copy
Edit

---

##  Fine-Tuning Pipeline (`finetuning.py`)

1. **Model Used:** `t5-small` (can replace with `gpt2` or other Seq2Seq models)
2. **Dataset:** Custom JSON (`instruction_dataset.json`) with:
   - `"instruction"`: what to do
   - `"input"`: the input text
   - `"output"`: the expected response
3. **Training Method:** Supervised LoRA fine-tuning using `peft`
4. **Trainer:** `Seq2SeqTrainer` from Hugging Face

###  Run Fine-Tuning:

```bash
python finetuning.py
After training, the model will be saved in:

bash
Copy
Edit
./final_model_lora/
 Inference UI with Streamlit (inference.py)
Use a simple and clean web UI to test the model post-finetuning.

🚀 Run the UI:
bash
Copy
Edit
streamlit run inference.py
You will be able to enter:

Instruction (e.g., "Summarize this", "Translate this")

Input text

And the model will generate a response using the fine-tuned weights.

🧰 Hugging Face AutoTrain (No-Code Fine-Tuning)
I also used Hugging Face AutoTrain to fine-tune the same model with zero code.

💡 You just:

Upload the dataset

Select model, task, hyperparameters

Deploy to Hugging Face Spaces or Hub

🧪 Great for beginners or quick experimentation.

📦 Model and Dataset Links
Resource	Link
🤗 Hugging Face Model	GPT-2 Fine-Tuned for Job Keyword Extraction
📂 GitHub Repository	Fine-Tuning Codebase
📊 Dataset File	instruction_dataset.json

🔗 Technologies Used
transformers, datasets, peft, torch, streamlit

LoRA (Low-Rank Adaptation)

Seq2SeqTrainer and Hugging Face Trainer APIs

Streamlit UI for real-time text generation

Hugging Face Hub for deployment

📌 To-Do & Future Enhancements
🔁 Add support for QLoRA and full PEFT benchmarking

📊 Integrate evaluation metrics like BLEU, ROUGE, etc.

🤖 LangChain integration with RAG pipeline

🔍 Hugging Face Spaces public demo

📦 Dockerize the full app for production


```
