Данные, которые передаются на фронт:

  id: number;

Ссылка на первоисточник -> primary_source_url?: string; 

Дата публикации первоисточника -> created_at?: string;

Текст новости -> text?: string;

Рейтинг доверенности первоисточника -> source_score?: number;

Количество СМИ, разместивших статью  -> times_published?: number;

Процент СМИ из списка, заблокированных Роскомнадзором  -> percentage_blacklist?: number;

Текст новости в первоисточнике ->   source_text?: string;

Рейтинг доверия первоисточника -> avg_sources_score?: number;

  reliable_sources_flag?: boolean;

  diagram_data?: {
    date: string;
    is_valid: boolean;
  }[];

Отличие статьи от первоисточника % -> plagiary_percentage?: string;  -> ezee_naeaw.text_tools.Article.unique


error_numerical_facts_score, error_ner_facts_score, facts_message = data_science_module.ds_module.text_source_facts_comparison(text, text_source)

  is_any_sentiment_delta?: true; -> bool(error_numerical_facts_score+error_ner_facts_score > 0) 

  facts?: string; -> facts_message

Количество грамматических ошибок -> grammatic_errors_count?: number; -> len(ezee_naeaw.text_tools.Article.spell))

Индекс "заспамленности" -> spam_index?: number; -> ezee_naeaw.text_tools.Article.seo["spam_percent"]

Индекс "воды" -> water_index?: number; -> ezee_naeaw.text_tools.Article.seo["water_percent"]




Индекс "эмоциональности" -> sentiment_index?: number; -> data_science_module.ds_module.text_source_sentiment_score(text, text_title, text_source, text_source_title)


negative_score, positive_score, neutral_score, skip_score, speech_score, clickbait_score, rationality_score, intuition_score = data_science_module.ds_module.get_sentiment_scores(
    text, text_title)

Индекс "разговорности" -> speech_index?: number; -> speech_score

Индекс "научности" -> intuition_index?: number; -> intuition_score

Индекс "кликбэйта" заголовка ->   clickbait_index?: number; -> data_science_module.clickbait.clickbait_predictor.Clickbait_predictor.get_clickbait_score(eng_text_title)

Индекс "интуитивности" -> rationality_index?: number; -> rationality_score

Индекс "фэйка" -> fake_index?: number; TODO -   implement score function

  date_added: string;

  date_updated: string;
