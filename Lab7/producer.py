import pika
from web_scraper import *


def send_urls_to_queue(urls):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='url_queue')

    for url in urls:
        channel.basic_publish(exchange='', routing_key='url_queue', body=url)

    print("Sent all URLs to queue.")

    connection.close()


if __name__ == "__main__":
    urls = start_web_scraping(2)
    # print(pages_found)
    # urls = start_web_scraping(pages_found)

    print(*(urls), sep='\n')
    print("Total: ", len(urls))
    send_urls_to_queue(urls)
