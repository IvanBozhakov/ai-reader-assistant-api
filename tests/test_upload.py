import pytest
import httpx

@pytest.mark.anyio
async def test_upload_pdf():
    file_path = "tests/sample.pdf"

    async with httpx.AsyncClient(base_url="http://127.0.0.1:8000") as client:
        with open(file_path, "rb") as f:
            response = await client.post(
                "/upload",
                files={"file": ("sample.pdf", f, "application/pdf")}
            )

    assert response.status_code == 200
    assert response.json()["filename"] == "sample.pdf"
    assert response.json()["chunks_uploaded"] == 2