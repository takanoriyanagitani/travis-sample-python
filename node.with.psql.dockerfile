FROM postgres:9.5.6 as p956

FROM node:6.9.5
COPY --from=p956 /usr/lib/postgresql/9.5/bin/psql /usr/bin/
COPY --from=p956 /usr/lib/x86_64-linux-gnu/libpq.so.5.9 /usr/lib/x86_64-linux-gnu/libpq.so.5
