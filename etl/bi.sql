CREATE TABLE IF NOT EXISTS controle_versao(
    cd_versao serial primary key,
    dt_versao date default now(),
    fato_versao integer default 1
);

CREATE TABLE IF NOT EXISTS dim_segmento(
    cd_segmento serial primary key,
    nm_segmento varchar(75) not null unique
);

CREATE TABLE IF NOT EXISTS dim_cliente(
    cd_cliente serial primary key,
    nr_cliente integer not null,
    nm_cliente varchar(100) not null,
    UNIQUE (nr_cliente, nm_cliente)
);

CREATE TABLE IF NOT EXISTS dim_localidade(
    cd_localidade serial primary key,
    nm_cidade varchar(75) not null,
    nm_estado varchar(2) not null,
    UNIQUE (nm_cidade, nm_estado)
);

CREATE TABLE IF NOT EXISTS dim_plano(
    cd_plano serial primary key,
    nm_plano varchar(15) not null unique
);

CREATE TABLE IF NOT EXISTS dim_dia(
    cd_dia serial primary key,
    dia integer not null unique
);

CREATE TABLE IF NOT EXISTS dim_mes(
    cd_mes serial primary key,
    nr_mes integer not null unique,
    nm_mes varchar(10) not null unique,
    sg_mes varchar(2) not null unique
);

CREATE TABLE IF NOT EXISTS dim_ano(
    cd_ano serial primary key,
    ano integer not null unique
);

CREATE TABLE IF NOT EXISTS fato_mrr(
    cd_fato serial primary key,
    cd_cliente integer not null REFERENCES dim_cliente(cd_cliente),
    cd_localidade integer not null REFERENCES dim_localidade(cd_localidade),
    cd_plano integer not null REFERENCES dim_plano(cd_plano),
    cd_dia integer not null REFERENCES dim_dia(cd_dia),
    cd_mes integer not null REFERENCES dim_mes(cd_mes),
    cd_ano integer not null REFERENCES dim_ano(cd_ano),
    periodicidade integer not null default 1,
    vl_mrr decimal(10,2) not null default 0,
    vl_cancelamento decimal(10,2) not null default 0,
    vl_expansao decimal(10,2) not null default 0,
    sn_novo integer not null default 0,
    sn_cancelado integer not null default 0,
    sn_renascido integer not null default 0
);

CREATE TABLE IF NOT EXISTS fato_segmento(
    cd_fato serial primary key,
    cd_segmento integer REFERENCES dim_segmento(cd_segmento),
    cd_localidade integer not null REFERENCES dim_localidade(cd_localidade),
    cd_plano integer not null REFERENCES dim_plano(cd_plano),
    cd_mes integer not null REFERENCES dim_mes(cd_mes),
    cd_ano integer not null REFERENCES dim_ano(cd_ano),
    vl_mrr decimal(10,2) not null default 0,
    vl_cancelamento decimal(10,2) not null default 0
);

INSERT INTO dashboard_dimdia (dia) VALUES (1),(2),(3),(4),(5),(6),(7),(8),(9),(10),(11),(12),(13),(14),(15),(16),(17),(18),(19),(20),(21),(22),(23),(24),(25),(26),(27),(28),(29),(30),(31) ON CONFLICT DO NOTHING;
INSERT INTO dashboard_dimmes (nr_mes, nm_nr_mes, nm_mes, sg_mes)
VALUES  (1, "01", 'Janeiro', 'Jan'),
        (2, "02", 'Fevereiro', 'Fev'),
        (3, "03", 'Março', 'Mar'),
        (4, "04", 'Abril', 'Abr'),
        (5, "05", 'Maio', 'Mai'),
        (6, "06", 'Junho', 'Jun'),
        (7, "07", 'Julho', 'Jul'),
        (8, "08", 'Agosto', 'Ago'),
        (9, "09", 'Setembro', 'Set'),
        (10, "10", 'Outubro', 'Out'),
        (11, "11", 'Novembro', 'Nov'),
        (12, "12", 'Dezembro', 'Dez')
ON CONFLICT DO NOTHING;
INSERT INTO dashboard_dimano (ano) 
VALUES  (1900),(1901),(1902),(1903),(1904),(1905),(1906),(1907),(1908),(1909),(1910),
        (1911),(1912),(1913),(1914),(1915),(1916),(1917),(1918),(1919),(1920),(1921),
        (1922),(1923),(1924),(1925),(1926),(1927),(1928),(1929),(1930),(1931),(1932),
        (1933),(1934),(1935),(1936),(1937),(1938),(1939),(1940),(1941),(1942),(1943),
        (1944),(1945),(1946),(1947),(1948),(1949),(1950),(1951),(1952),(1953),(1954),
        (1955),(1956),(1957),(1958),(1959),(1960),(1961),(1962),(1963),(1964),(1965),
        (1966),(1967),(1968),(1969),(1970),(1971),(1972),(1973),(1974),(1975),(1976),
        (1977),(1978),(1979),(1980),(1981),(1982),(1983),(1984),(1985),(1986),(1987),
        (1988),(1989),(1990),(1991),(1992),(1993),(1994),(1995),(1996),(1997),(1998),
        (1999),(2000),(2001),(2002),(2003),(2004),(2005),(2006),(2007),(2008),(2009),
        (2010),(2011),(2012),(2013),(2014),(2015),(2016),(2017),(2018),(2019),(2020),
        (2021),(2022),(2023),(2024),(2025),(2026),(2027),(2028),(2029),(2030),(2031),
        (2032),(2033),(2034),(2035),(2036),(2037),(2038),(2039),(2040),(2041),(2042),
        (2043),(2044),(2045),(2046),(2047),(2048),(2049),(2050)
ON CONFLICT DO NOTHING;