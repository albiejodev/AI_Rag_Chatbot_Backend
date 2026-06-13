## Architecture

```text
                        ┌─────────────────┐
                        │   User Upload   │
                        │      PDF        │
                        └────────┬────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │      PDF Service        │
                    │   PyPDFLoader Extract   │
                    └────────┬────────────────┘
                             │
                             ▼
                    ┌─────────────────────────┐
                    │     Chunk Service       │
                    │ RecursiveTextSplitter   │
                    └────────┬────────────────┘
                             │
                             ▼
                    ┌─────────────────────────┐
                    │   Embedding Service     │
                    │ Gemini Embedding Model  │
                    └────────┬────────────────┘
                             │
                             ▼
                    ┌─────────────────────────┐
                    │       ChromaDB          │
                    │   Vector Storage Layer  │
                    └────────┬────────────────┘
                             │
                             │
              ┌──────────────┴──────────────┐
              │                             │
              ▼                             ▼

      ┌───────────────┐            ┌────────────────┐
      │ Search Query  │            │ Chat Question  │
      └───────┬───────┘            └───────┬────────┘
              │                            │
              ▼                            ▼
      ┌────────────────┐          ┌────────────────┐
      │ Vector Search  │          │ Vector Search  │
      │ Top K Chunks   │          │ Top K Chunks   │
      └───────┬────────┘          └───────┬────────┘
              │                            │
              │                            ▼
              │                 ┌────────────────────┐
              │                 │    RAG Service     │
              │                 │ Context Injection  │
              │                 └─────────┬──────────┘
              │                           │
              │                           ▼
              │                 ┌────────────────────┐
              │                 │ Gemini 2.5 Flash   │
              │                 │ Answer Generation  │
              │                 └─────────┬──────────┘
              │                           │
              ▼                           ▼

      Search Results         Answer + Source Citations
```
