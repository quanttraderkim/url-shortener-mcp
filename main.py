import requests
from fastmcp import FastMCP

# MCP 서버 생성
mcp = FastMCP("URLShortener")

@mcp.tool
def shorten_url(long_url: str) -> dict:
    """
    긴 URL을 받아 짧은 TinyURL로 변환합니다.

    Args:
        long_url: 단축하고 싶은 원본 URL.

    Returns:
        단축된 URL이 포함된 딕셔너리. 실패 시 에러 메시지 포함.
    """
    api_url = "http://tinyurl.com/api-create.php"
    try:
        response = requests.get(api_url, params={'url': long_url})
        if response.status_code == 200:
            return {"short_url": response.text}
        else:
            return {"error": f"API 요청 실패: 상태 코드 {response.status_code}"}
    except requests.RequestException as e:
        return {"error": f"요청 중 에러 발생: {e}"}

if __name__ == "__main__":
    mcp.run()
