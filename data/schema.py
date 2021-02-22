tables = ["title t", "movie_companies mc", "cast_info ci", "movie_info mi", "movie_info_idx mi_idx", "movie_keyword mk"]

table_dic = {"t": "title t",
             "mc": "movie_companies mc",
             "ci": "cast_info ci",
             "mi": "movie_info mi",
             "mi_idx": "movie_info_idx mi_idx",
             "mk": "movie_keyword mk"}

ban_tables = ["movie_info mi", "movie_info_idx mi_idx"]

attributes = {"title t": ["t.id", "t.kind_id", "t.production_year"],
              "movie_companies mc": ["mc.id", "mc.company_id", "mc.movie_id", "mc.company_type_id"],
              "cast_info ci": ["ci.id", "ci.movie_id", "ci.person_id", "ci.role_id"],
              "movie_info mi": ["mi.id", "mi.movie_id", "mi.info_type_id"],
              "movie_info_idx mi_idx": ["mi_idx.id", "mi_idx.movie_id", "mi_idx.info_type_id"],
              "movie_keyword mk": ["mk.id", "mk.movie_id", "mk.keyword_id"]}

all_attributes = ["t.id", "t.kind_id", "t.production_year", "", "",
                  "mc.id", "mc.company_id", "mc.movie_id", "mc.company_type_id", "",
                  "ci.id", "ci.movie_id", "ci.person_id", "ci.role_id", "",
                  "mi.id", "mi.movie_id", "mi.info_type_id", "", "",
                  "mi_idx.id", "mi_idx.movie_id", "mi_idx.info_type_id", "", "",
                  "mk.id", "mk.movie_id", "mk.keyword_id", "", "",
                  "", "", "", "", "",
                  "", "", "", "", ""]

min_max = {'t.id': (1, 2528312), 't.kind_id': (1, 7), 't.production_year': (1880, 2019),
           'mc.id': (1, 2609129), 'mc.company_id': (1, 234997), 'mc.movie_id': (2, 2525745),
           'mc.company_type_id': (1, 2),
           'ci.id': (1, 36244344), 'ci.movie_id': (1, 2525975), 'ci.person_id': (1, 4061926), 'ci.role_id': (1, 11),
           'mi.id': (1, 14835720), 'mi.movie_id': (1, 2526430), 'mi.info_type_id': (1, 110),
           'mi_idx.id': (1, 1380035), 'mi_idx.movie_id': (2, 2525793), 'mi_idx.info_type_id': (99, 113),
           'mk.id': (1, 4523930), 'mk.movie_id': (2, 2525971), 'mk.keyword_id': (1, 134170)}

cardinality = {"title t": 2528312,
               "movie_companies mc": 2609129,
               "cast_info ci": 36244344,
               "movie_info mi": 14835720,
               "movie_info_idx mi_idx": 1380035,
               "movie_keyword mk": 4523930,
               "join": 460456073}
