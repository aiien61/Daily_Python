import subprocess

# Mac OS X
# calc_proc = subprocess.Popen(['open', '/System/Applications/Calculator.app'])

# print(calc_proc.poll() == None)
# print(calc_proc.wait())
# print(calc_proc.poll())

subprocess.Popen(['open', '/Users/mac/Desktop/scheduling algorithms.pdf',
                 '/System/Applications/Calculator.app'])
