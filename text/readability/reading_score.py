# https://pypi.org/project/py-readability-metrics/

# install the package:
# pip install py-readability-metrics
# python -m nltk.downloader punkt

from readability import Readability

text = "If we had started preparing next year's national budget today, we would not be able to afford so much. The budget, which has been submitted to the Parliament, is based on the economic growth forecasts made in June. Politicians, however, do nIf we had started preparing next year's national budget today, we would not be able to afford so much. The budget, which has been submitted to the Parliament, is based on the economic growth forecasts made in June. Politicians, however, do not plan any adjustments for the time being and are satisfied, reports Latvian Television's De Facto on October 27. The Latvian central bank (Bank of Latvia) this month significantly lowered its gross domestic product (GDP) forecast for this year from 1.8% to 0.6%, and also for the next few years. The budget deficit could exceed the symbolic 3% threshold already this year, according to the Bank of Latvia.ot plan any adjustments for the time being and are satisfied, reports Latvian Television's De Facto on October 27."

r = Readability(text)
f = r.flesch()
print(f.score)
print(f.ease)
print(f.grade_levels)