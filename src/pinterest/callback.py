from fastapi import FastAPI, Request
from src.pinterest.auth import PinterestAuth

app = FastAPI()


@app.get("/callback")
async def pinterest_callback(request: Request):

    code = request.query_params.get("code")

    if not code:
        return {
            "success": False,
            "message": "No authorization code received."
        }

    try:
        auth = PinterestAuth()

        # Exchange authorization code for access token
        token_data = auth.exchange_code_for_token(code)

        access_token = token_data.get("access_token")
        refresh_token = token_data.get("refresh_token")

        if not access_token:
            return {
                "success": False,
                "message": "Pinterest did not return an access token.",
                "response": token_data,
            }

        # Save the new access token to .env
        with open(".env", "r", encoding="utf-8") as file:
            env_content = file.read()

        lines = env_content.splitlines()
        updated_lines = []

        token_saved = False
        refresh_saved = False

        for line in lines:

            if line.startswith("PINTEREST_ACCESS_TOKEN="):
                updated_lines.append(
                    f"PINTEREST_ACCESS_TOKEN={access_token}"
                )
                token_saved = True

            elif line.startswith("PINTEREST_REFRESH_TOKEN="):
                if refresh_token:
                    updated_lines.append(
                        f"PINTEREST_REFRESH_TOKEN={refresh_token}"
                    )
                    refresh_saved = True
                else:
                    updated_lines.append(line)

            else:
                updated_lines.append(line)

        if not token_saved:
            updated_lines.append(
                f"PINTEREST_ACCESS_TOKEN={access_token}"
            )

        if refresh_token and not refresh_saved:
            updated_lines.append(
                f"PINTEREST_REFRESH_TOKEN={refresh_token}"
            )

        with open(".env", "w", encoding="utf-8") as file:
            file.write("\n".join(updated_lines) + "\n")

        return {
            "success": True,
            "message": "Pinterest authorization completed successfully!",
            "token_saved": True,
            "refresh_token_saved": bool(refresh_token),
            "scopes": token_data.get("scope"),
        }

    except Exception as error:

        return {
            "success": False,
            "message": "Failed to exchange authorization code.",
            "error": str(error),
        }