f = open('file1.txt',  'a', encoding= 'UTF-8')
a = f.write(input('Введіть рядок, який хочете записати в файл:'))
f.close()
