ranked_pool = sorted(

    pool,

    key=lambda item: item["uncertainty"],

    reverse=True,

 )



batch_size = 2

query_batch = ranked_pool[:batch_size]



for item in query_batch:

    print(item["id"], round(item["uncertainty"], 2))
