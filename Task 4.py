# Вот строка  [] удалите из нее все повторяющиеся буквы и выведете строку уникальных букв

s = "rewlkdfsklgjdflkjglkdsfjgkldfsjglkjeroitewuiotujdigjsdfklg;klsdfgkl;jsdfkl;gjldk;sfjgjlk;sdfjlk;gjsdfl;kgl;kdsfjgl;kjsdfl;kgjl;sdfkjg;lkjsdflbvjdfslkglkrewjhtiowerjutioerutopiytuilyhjdsfl;kghjl;sdkf;gjdffffffffflkgjlkdfjglkasjdfoitweigheripjgierglisjdfkjlghsdfkj;l;hgkljasdhfglk;hsdfkjlghlk;sdfhg;kljsdflkgjlk;sdfjgl;ksdfjl;kgjsdfl;kjglk;sdfjgkjsdfl;kgjs;dlkfjgoiw3eujtio34wuytiergoijherjhlgjsdflkjgkl;dfjgkl;sdfjkl;gjsdf;lkjg;lsjeriotuerl;kjdsfkl;jgh;lksdfjg;lksdfjg;lksdfkjg;lkjreopyulidsjfl;kghjs;ldkjg;lkkjr5l;h;kljyhkl;rirtiririiiiiiiiiiiiiierwtsj;kldfjg;lksdfjgl;ksdjfl;gj;lsdfjg;lk"
s_new = ''
s_new1 = ''
for i in range(len(s)):
    if s_new.find(s[i]) == -1 and s[i] != ' ':
        s_new += s[i]
print(s_new)

#Какая буквенная подпоследовательность одинаковых символов самая длинная


#Напишите функцию которая будет удалять заданную букву из строки и протестируйте ее на вышеприведенной строчке
n = input("Какую букву удалить? ")
for i in range(len(s)):
    if s[i] != n:
        s_new1 += s[i]
print(s_new1)