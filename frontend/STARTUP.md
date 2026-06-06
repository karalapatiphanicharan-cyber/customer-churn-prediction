# ChurnGuard AI Frontend - Startup Guide

## Installation

1. `cd frontend`
2. `npm install`

## Environment Setup

1. `cp .env.example .env`
2. Ensure `VITE_API_BASE_URL=http://localhost:8000`

## Running

1. Start backend: `uvicorn backend.app:app --reload --port 8000`
2. Start frontend: `npm run dev`
