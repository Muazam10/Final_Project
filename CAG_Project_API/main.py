from fastapi import FastAPI
from src.routers import data_handler
from fastapi.responses import HTMLResponse

app = FastAPI(
    title="CAG Project API Chat With Your PDF",
    description="API for uploading PDFs, querying content via LLM, and managing data",
    version="0.1.0",
)

app.include_router(
    data_handler.router,
    prefix="/api/v1",
    tags=["Data Handling And Chat with PDF"],
)

@app.get("/", response_class=HTMLResponse, tags=["Root"])
def read_root():
    """
    Provides a simple HTML welcome page with a link to swagger (OpenAPI) docs.
    """
    html_content = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>CAG Project API</title>

    <link rel="icon" href="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSzMFgjQjonPsKrE5IKLXX4zYHm1IxMwAPsvw&s" type="image/png" />

    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <!-- Google Font -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet" />
    <style>
      * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
      }

      body {
        font-family: 'Inter', sans-serif;
        background: linear-gradient(135deg, #dbeafe, #f0fdfa);
        min-height: 100vh;
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
        position: relative;
      }

      /* Subtle floating circles */
      body::before,
      body::after {
        content: "";
        position: absolute;
        border-radius: 50%;
        background: rgba(0, 123, 255, 0.15);
        animation: float 6s ease-in-out infinite;
        z-index: 0;
      }

      body::before {
        width: 200px;
        height: 200px;
        top: -50px;
        left: -50px;
      }

      body::after {
        width: 150px;
        height: 150px;
        bottom: -40px;
        right: -40px;
      }

      @keyframes float {
        0%, 100% {
          transform: translateY(0px);
        }
        50% {
          transform: translateY(15px);
        }
      }

      .container {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(20px);
        border-radius: 20px;
        padding: 3rem 2rem;
        max-width: 600px;
        width: 90%;
        text-align: center;
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.1);
        z-index: 1;
        animation: fadeInUp 1s ease-out;
      }

      h1 {
        font-size: 2.5rem;
        color: #1e3a8a;
        margin-bottom: 1rem;
      }

      p {
        font-size: 1.15rem;
        color: #333;
        margin-bottom: 2rem;
      }

      a {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        background: linear-gradient(135deg, #007bff, #00c6ff);
        color: white;
        text-decoration: none;
        font-weight: 600;
        font-size: 1rem;
        padding: 0.75rem 1.5rem;
        border-radius: 10px;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        box-shadow: 0 5px 15px rgba(0, 123, 255, 0.4);
      }

      a:hover {
        transform: translateY(-3px) scale(1.03);
        box-shadow: 0 8px 20px rgba(0, 123, 255, 0.5);
      }

      a span {
        margin-right: 0.5rem;
        font-size: 1.2rem;
      }

      @keyframes fadeInUp {
        from {
          opacity: 0;
          transform: translateY(20px);
        }
        to {
          opacity: 1;
          transform: translateY(0);
        }
      }

      @media (max-width: 480px) {
        h1 {
          font-size: 2rem;
        }
        p {
          font-size: 1rem;
        }
      }
    </style>
  </head>
  <body>
    <div class="container">
      <h1>🚀 Welcome to the CAG Project API</h1>
      <p>Start exploring our live interactive documentation:</p>
      <a href="/docs" target="_blank">
        <span>🔍</span> Swagger UI (OpenAPI Docs)
      </a>
    </div>
  </body>
</html>

"""
    return HTMLResponse(content=html_content, status_code=200)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app, host="127.0.0.1", port=8001
    )