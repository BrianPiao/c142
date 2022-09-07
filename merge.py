import csv
with open("movies.csv") as f:
    r = csv.reader(f)
    d = list(r)
    allmov = d[1:]
    headers = d[0]
headers.append("posted_link")
with open("final.csv", "a+") as f:
    r = csv.writer(f)
    r.writerow(headers)
with open("movie_links.csv") as f:
    r = csv.reader(f)
    d = list(r)
    all_movie_links = d[1:]
for i in allmov:
    #Searching column "Original title" in "movies.csv" and then iterating that in "movie_links.csv"
    pf = any(i[8] in mli for mli in all_movie_links)
    if pf:
        for pp in all_movie_links:
            if i[8] == pp[0]:
                i.append(pp)
                if len(i) == 28:
                    with open("final.csv", "a+") as f:
                        r = csv.writer(f)
                        r.writerow(headers)