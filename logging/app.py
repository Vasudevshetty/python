import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[logging.FileHandler("app.log"), logging.StreamHandler()],
)

logger = logging.getLogger("ArithmethicLogger")


def add(a, b):
    result = a + b
    logger.debug(f"Adding {a} and {b}: {result}")
    return result

def subtract(a, b):
    result = a - b
    logger.debug(f"Subtracting {b} from {a}: {result}")
    return result

def multiply(a, b):
    result = a * b
    logger.debug(f"Multiplying {a} and {b}: {result}")
    return result

def divide(a, b):
    try:
        result = a / b
        logger.debug(f"Dividing {a} by {b}: {result}")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero error")
        return None
    
add(5, 3)
subtract(10, 4)
multiply(2, 6)
divide(8, 2)
divide(8, 0)