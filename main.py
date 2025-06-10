import asyncio
import queue
import threading
import logging
import argparse

from src.core.generator import NewsGenerator
from src.audio.player import play_audio_from_queue

def main():
    parser = argparse.ArgumentParser(description="Generate a continuous news broadcast stream.")
    parser.add_argument("--topic", type=str, help="Optional topic to filter and focus news generation.")
    parser.add_argument("--guidance", type=str, help="Optional guidance for refining the news script.")
    parser.add_argument("--fetch_interval", type=int, default=15, help="Minutes to wait between fetching new feeds.")
    parser.add_argument("--persona", type=str, default="persona.yaml", help="Path to the persona YAML file.")

    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[logging.FileHandler('news.log'), logging.StreamHandler()]
    )
    
    audio_queue = queue.Queue()

    player_thread = threading.Thread(target=play_audio_from_queue, args=(audio_queue,), daemon=True)
    player_thread.start()

    generator = NewsGenerator(
        audio_queue=audio_queue,
        topic=args.topic,
        guidance=args.guidance,
        persona_file=args.persona # Pass the persona file to the generator
    )

    logging.info("Starting the news generator. Press Ctrl+C to stop.")
    try:
        asyncio.run(generator.run_continuous(fetch_interval_minutes=args.fetch_interval))
    except KeyboardInterrupt:
        logging.info("Shutting down the news generator.")

if __name__ == "__main__":
    main()
