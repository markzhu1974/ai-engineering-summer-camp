import argparse
import pickle

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

from config import INDEX_PATH, RESULTS_DIR, ensure_dirs


def load_index():
    if not INDEX_PATH.exists():
        raise FileNotFoundError(
            f"Index not found: {INDEX_PATH}\n"
            "Please run: python src/build_index.py"
        )
    with INDEX_PATH.open("rb") as f:
        return pickle.load(f)


def retrieve(question: str, top_k: int = 3):
    payload = load_index()
    vectorizer = payload["vectorizer"]
    matrix = payload["matrix"]
    chunks = payload["chunks"]

    query_vec = vectorizer.transform([question])
    scores = cosine_similarity(query_vec, matrix).flatten()
    top_indices = scores.argsort()[::-1][:top_k]

    results = []
    for rank, idx in enumerate(top_indices, start=1):
        item = dict(chunks[idx])
        item["rank"] = rank
        item["score"] = float(scores[idx])
        results.append(item)
    return results


def build_answer(question: str, contexts):
    context_text = "\n\n".join(
        f"[{item['rank']}] source={item['source']} score={item['score']:.4f}\n{item['text']}"
        for item in contexts
    )
    answer = f"""问题：{question}

基于知识库检索到的内容，参考答案如下：

{contexts[0]['text']}

参考来源：
{context_text}
"""
    return answer


def ask(question: str, top_k: int = 3):
    ensure_dirs()
    contexts = retrieve(question, top_k=top_k)
    answer = build_answer(question, contexts)

    result_path = RESULTS_DIR / "last_rag_answer.md"
    result_path.write_text(answer, encoding="utf-8")

    rows = pd.DataFrame(contexts)
    rows.to_csv(RESULTS_DIR / "last_retrieval_results.csv", index=False, encoding="utf-8-sig")

    return answer


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--question", required=True, help="Question to ask the RAG system")
    parser.add_argument("--top-k", type=int, default=3)
    args = parser.parse_args()

    answer = ask(args.question, top_k=args.top_k)
    print(answer)


if __name__ == "__main__":
    main()

