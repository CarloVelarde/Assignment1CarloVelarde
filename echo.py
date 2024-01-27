def echo(text: str, repetitions:int = 3) -> str:
   """Imitate a real-world echo."""
   echoed_text = ''

   # Checks if the input is smaller than repeititons
   start_index = max(0, len(text) - repetitions)

   for i in range(repetitions):
      echoed_text += text[start_index:] + '\n'
      start_index+=1
   return echoed_text
      



if __name__ == "__main__":
   text = input("Yell something at the mountain: ")
   print(echo(text))
