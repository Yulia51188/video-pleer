# Видеоплеер

Современный встроенный видеоплеер для вашего сайта. Плеер обладает стандартными кнопками управления, позволяющими воспроизводить/останавливать видео, включать/выключать звук, а также переходить в полноэкранный режим.

[Попробовать](https://yulia51188.github.io/video-pleer/)

![image](/demo/demo_image.png)

## Ресурсы

- [Библиотека для создания видеоплеера](https://github.com/devmanorg/video-player-jslib), использующая:
  - [jQuery](https://jquery.com/)
  - [Playable](https://wix.github.io/playable/)
- [Livereload](http://livereload.com/) - отслеживание изменений в файлах для удобства разработки
- [Fontawesome](https://fontawesome.ru/get-started/) - набор шрифтов для иконок кнопок видеоплеера

## Разработчикам

Для запуска плеера на локальной машине:
- склонируйте репозиторий
- установите библиотеку `livereload`:
```bash
$ pip install livereload
```
- запустите сервер `livereload`:

```bash
$ livereload dist
[I 220222 11:24:03 server:335] Serving on http://127.0.0.1:35729
[I 220222 11:24:03 handlers:62] Start watching changes
[I 220222 11:24:03 handlers:64] Start detecting changes

```
- откройте в браузере указанную страницу [http://127.0.0.1:35729](http://127.0.0.1:35729)

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
