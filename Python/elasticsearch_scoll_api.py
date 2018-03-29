from elasticsearch import Elasticsearch


def scoll_snippet():
    """
    snippet for elasticsearch scoll api
    """

    # Initialize elasticsearch
    es = Elasticsearch()

    # Initialize the scroll
    page = es.search(
            index='yourIndex',
            doc_type='yourType',
            scroll='2m',
            size=1000,
            body={
                  "query": {
                        "match_all": {}
                    }
                })

    sid = page['_scroll_id']
    scroll_size = page['hits']['total']

    # Start scrolling
    while scroll_size > 0:
        print("Scrolling...")
        page = es.scroll(scroll_id=sid, scroll='2m')
        # Update the scroll ID
        sid = page['_scroll_id']
        # Get the number of results that we returned in the last scroll
        scroll_size = len(page['hits']['hits'])
        print "scroll size: " + str(scroll_size)
        # Do something with the obtained page
        # ......
        # ......

if __name__ == "__main__":
    main()
