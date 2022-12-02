from fastapi import HTTPException

def http_500_handler(ex: Exception, function: str):
    exception_class = f"{ex.__class__}"
    error_message = f"{ex.detail if hasattr(ex, 'detail') else ex}"
    raise HTTPException(
        status_code=500,
        detail=f"Unable to {function}: \n "
        f"exception class: {exception_class} \n "
        f"error message: {error_message}",
    )
