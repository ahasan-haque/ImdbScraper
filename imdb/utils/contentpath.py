

name_to_xpath_mapper = {
    'movie_name': '//h1[@itemprop = "name"]/text()',
    'release_year':'//span[@id = "titleYear"]/a/text()',
    'rating': '//span[@itemprop="ratingValue"]/text()',
    'total_votes': '//span[@itemprop="ratingCount"]/text()',
    'director_name': '//span[@itemprop="director"]/a/span/text()',
    'top_actors': '//span[@itemprop="actors"]/a/span/text()',
    'storyline': '//div[@itemprop="description"]/p/text()',
    'tagline':'//h4[text() = "Taglines:"]/following-sibling::text()',
    'genres': '//div[@itemprop="genre"]/a/text()',
    'country': '//h4[text() = "Country:"]/following::a/text()',
    'languages':'//h4[text() = "Language:"]/following-sibling::a/text()',
    'filming_locations': '//h4[text() = "Filming Locations:"]/following-sibling::a/text()',
    'budget': '//h4[text() = "Budget:"]/following-sibling::text()',
    'gross_income': '//h4[text() = "Gross:"]/following-sibling::text()',
    'color': '//h4[text() = "Color:"]/following-sibling::a/text()',
    'production_company': '//h4[text() = "Production Co:"]/following-sibling::span[@itemprop="creator"]/a/span/text()',
    'runtime': '//h4[text() = "Runtime:"]/following::time/text()',
    'metascore': '//div[contains(@class,"metacriticScore")]/span/text()'
}