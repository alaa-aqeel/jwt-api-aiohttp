import asyncio
from application import create_app, web


HOST = '0.0.0.0'
PORT = 8080


async def main():

	app = create_app()

	runner = web.AppRunner(app)
	await runner.setup()

	site = web.TCPSite(runner, HOST, PORT)
	await site.start()

	return runner


if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	runner = loop.run_until_complete(main())

	try:
		print(f'Start Server: http://{HOST}:{PORT}/')
		loop.run_forever()
	except KeyboardInterrupt:
		loop.run_until_complete(runner.cleanup())

	loop.close()