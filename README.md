# Dart Quest — Lab 01

Standalone 15-mission Dart beginner lab, hosted from **iamg2r2/dart**.

## Pages

- Student app: `index.html` → https://iamg2r2.github.io/dart/
- Teacher dashboard: `teacher.html` → https://iamg2r2.github.io/dart/teacher.html

## Publish

1. Visit repository **Settings → Pages**, then choose **Deploy from a branch**, `main`, `/(root)`, and Save.
2. Under repository **Settings → General**, enable **Issues**.
3. Under **Settings → Actions → General**, enable Actions and set workflow permissions to **Read and write permissions** if writes fail.
4. Create the issue label `lab01-submission` if it is missing.
5. Students enter their register numbers, complete each mission, make a separate GitHub repository, and file their submission via the **Submit** link inside the student app.
6. The workflow `.github/workflows/collect-submissions.yml` processes issue submissions and updates `submissions.json`. The teacher page can then refresh to see them.

## Storage and security

- `submissions.json` contains only `regnumber` and `github_repo`.
- GitHub Issues contains the public submission form and standard GitHub issue metadata.
- Browser-based register-number entry is identification only, **not authentication**.
- Mission completion and XP are local browser data; they are **not visible to the teacher remotely**.
- The Teacher Desk is a separate public webpage. GitHub Pages does not provide a teacher-only login, and the JSON is public for a public repository. Do **not** assume the dashboard is private.
- This setup uses GitHub Issues and Actions to update JSON because static GitHub Pages cannot safely write repository files from the browser.
- For true teacher-only access or live analytics, introduce authenticated backend storage when moving the app into g2r2 Academy.

## Curriculum

15 missions cover `main()`, `print()`, variables, `String`, `int`, `double`, `bool`, `num`, `dynamic`, `final`, `const`, null safety, `??`, string interpolation, arithmetic, conversion and `stdin.readLineSync()`. No `if/else`, loops, collections or custom functions.

Missions 13–15 require a local Dart console rather than DartPad.
