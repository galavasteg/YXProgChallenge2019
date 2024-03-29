"""
ФОРМАТ ВВОДА
Это интерактивная задача. В ней вам необходимо
сообщать системе (выводом строки в stdout), на
какой из перекрестков приехал водитель. В ответ
система выдает набор соседних улиц, на которые
можно проехать с текущего перекрестка.

При запуске система пишет ровно одну строку с
одним числом N - количество перекрестков в городе.

Далее система ожидает вывод программы - следующий
перекресток, который необходимо посетить (более
подробно формат описан в секции "Формат вывода").
В ответ на это система выдает строку с числами,
разделенными через пробел. Первое число в строке
K - число перекрестков, до которых можно доехать
из текущего. Далее идут через пробел номера этих
перекрестков.

Водитель всегда начинает с перекрестка с номером 0.

Ограничения:
3 ≤ N ≤ 500
1 ≤ K ≤ N-1
Максимальное количество итераций (количество
посещенных вершин): 5000

Если превышено количество итераций, система
остановит выполнение и результатом задачи будет PE.


ФОРМАТ ВЫВОДА
Система ожидает на выходе программы на каждой
итерации ровно одну строку с одним числом - номером
очередного перекрестка. Если ваша программа посетила
все перекрестки, тогда необходимо вывести -1 вместо
номера перекрестка. Это будет признаком того, что
необходимо завершить работу. После этого система не
будет ничего присылать на вход.

Если система получит на вход номер перекрестка, в
который нельзя проехать из текущего - тогда система
остановит выполнение и выдаст ошибку WA.


ПРИМЕЧАНИЯ
Некоторые улицы города могут быть односторонними. Ни
одна улица не может начинаться и заканчиваться в
одном и том же перекрестке. Все перекрестки в городе
нумеруются с 0 до N-1 включительно.

Гарантируется, что все перекрестки возможно посетить
за максимальное число итераций.

Пример:

3
> 0
1 1
> 1
1 2
> 2
1 0
> -1

Пояснения к примеру:
В примере символом > указан выход программы, который
идет на вход системе. Следом за этой строкой идут
входные данные в программу, которые выдает система в
ответ на это.
В первой строке система сообщает, что в городе всего
3 перекрестка. Первым мы обязаны посетить перекресток
с номером 0. В ответ система сообщает, что из него
можно перейти только в один другой перекресток - с
номером 1.
Далее за 3 шага мы посещаем все 3 перекрестка,
поэтому дальше можно завершить работу. Для этого
программа выводит число -1.
"""