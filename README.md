# ett-exercises-export

In 2021 I made lots of exercises for the English department at KU Leuven. Because online exercise platforms seemingly change every three years, these exercises have been moved from platform to platform several times now. I have decided to make them human readable from my source files, which should speed up the moving process now and in the future.

```
usage: vocpopuliconv.py [-h] exercise_folder header output_filename

vocpopuliconv - convert vocpopuli json exercises to an easy Manon-readable format

positional arguments:
  exercise_folder  the exercise file which will be converted
  header           the header for the top of the file
  output_filename  where should the rendered html go to? include extension

options:
  -h, --help       show this help message and exit
```

The input is the directory where all JSON files I made in vocpopuli are stored. The output will be a HTML file.

I cannot include the exercises themselves for several reasons, but I have them stored away. Shoot me a message if you need them.

I used Anthe Intelligence to write this script. No LLM mumbo jumbo thank you very much