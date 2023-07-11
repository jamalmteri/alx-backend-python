#!/usr/bin/env python3

import asyncio
import random

async def async_generator():
    for _ in range(10):
        await asyncio.sleep(1)  # Asynchronously wait for 1 second
        yield random.randint(0, 10)  # Generate and yield a random number between 0 and 10

# Example usage
async def main():
    async for number in async_generator():
        print(number)

asyncio.run(main())

