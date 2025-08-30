# ObsiRAG

A full-stack AI-powered study assistant that helps you query your university notes using natural language. Built with FastAPI (Python) for the backend and Next.js (React/TypeScript) for the frontend.

## Features
- **RAG (Retrieval-Augmented Generation):** Query your notes using LLMs and semantic search.
- **FastAPI Backend:** Handles note ingestion, vector storage, and AI-powered responses.
- **Next.js Frontend:** Modern, responsive chat UI for interacting with your study assistant.
- **Dockerized:** Easy to run locally or deploy anywhere.
- **Makefile:** Simple commands for setup, running, and cleaning.

## Getting Started

### Prerequisites
- Python 3.11+
- Node.js 18+
- Docker (optional, for containerized runs)

### Backend Setup
1. **Clone the repo:**
	```sh
	git clone https://github.com/Ayush272002/ObsiRag.git
	cd ObsiRag/backend
	```
2. **Create a `.env` file:**
	```env
	DATABASE_URL='your_postgres_url'
	GROQ_API_KEY='your_groq_api_key'
	```
3. **Install dependencies and run:**
	```sh
	make install
	make start
	```
4. **Or run with Docker:**
	```sh
	docker build -t obsi-backend .
	docker run -p 8000:8000 -e DATABASE_URL='...' -e GROQ_API_KEY='...' obsi-backend
	```

### Frontend Setup
1. **Install dependencies:**
	```sh
	cd frontend
	pnpm install
	```
2. **Run the frontend:**
	```sh
	pnpm dev
	```
3. **Open [http://localhost:3000](http://localhost:3000) in your browser.**

## Project Structure
```
ObsiRAG/
├── backend/
│   ├── main.py
│   ├── api/
│   ├── db/
│   ├── rag/
│   ├── scripts/
│   ├── requirements.txt
│   ├── Dockerfile
│   └── ...
├── frontend/
│   ├── app/
│   ├── components/
│   ├── package.json
│   └── ...
└── README.md
```

## Useful Commands
- `make install` — Set up Python venv and install backend dependencies
- `make start` — Start the FastAPI backend
- `make clean` — Remove venv and __pycache__
- `docker build -t obsi-backend .` — Build Docker image (from backend dir)
- `docker run -p 8000:8000 ... obsi-backend` — Run backend in Docker
- `pnpm install` — Install frontend dependencies
- `pnpm dev` — Start frontend dev server

## License
This project is licensed under the ISC License. See the [LICENSE](LICENSE) file for details.

## Contributing
Contributions are welcome! Please open an issue or pull request.

