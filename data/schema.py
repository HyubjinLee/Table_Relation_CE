tables = ["title t", "movie_companies mc", "cast_info ci", "movie_info mi", "movie_info_idx mi_idx", "movie_keyword mk"]

columns = {"title t": ["t.id", "t.kind_id", "t.production_year"],
           "movie_companies mc": ["mc.id", "mc.company_id", "mc.movie_id", "mc.company_type_id"],
           "cast_info ci": ["ci.id", "ci.movie_id", "ci.person_id", "ci.role_id"],
           "movie_info mi": ["mi.id", "mi.movie_id", "mi.info_type_id"],
           "movie_info_idx mi_idx": ["mi_idx.id", "mi_idx.movie_id", "mi_idx.info_type_id"],
           "movie_keyword mk": ["mk.id", "mk.movie_id", "mk.keyword_id"]}
