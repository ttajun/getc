import sys
import numpy
import argparse
import asyncio
import aiohttp

responseLength = list()


async def get_length(url, insecure, timeout):
    timeout = aiohttp.ClientTimeout(timeout)
    async with aiohttp.ClientSession() as sess:
        async with sess.get(url, ssl=insecure, timeout=timeout) as res:
            text = await res.text()
            responseLength.append(len(text))


async def main():

    sys.tracebacklimit = 0
    parser = argparse.ArgumentParser(
        description='Count http GET response data'
    )
    parser.add_argument(
        "urls",
        metavar="URL",
        nargs='+',
        help='test urls'
    )
    parser.add_argument(
        '-t',
        '--timeout',
        type=int,
        help='timeout (second)',
        default=300
    )
    parser.add_argument(
        '-k',
        '--insecure',
        help='skip TLS/SSL',
        action="store_true"
    )

    args = parser.parse_args()

    futures = [asyncio.ensure_future(
        get_length(url, not args.insecure, args.timeout)) for url in args.urls]

    await asyncio.gather(*futures)

    print("평균:", numpy.mean(responseLength))
    print("표준편차:", numpy.std(responseLength))

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.run_until_complete(asyncio.sleep(0))
loop.close()
