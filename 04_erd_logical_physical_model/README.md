# ERD logical and physical model

TODO: video

**Part 1 theory**

<!-- <a href="https://youtu.be/ZMNRnMhWSgY" target="_blank">
  <img src="https://github.com/kokchun/assets/blob/main/data_modeling/ldm_pdm.png?raw=true" alt="data modeling ldm, pdm" width="600">
</a> -->

**Part 2 practical implementation**

<!-- <a href="https://youtu.be/nA4Hs08EOTI" target="_blank">
  <img src="https://github.com/kokchun/assets/blob/main/data_modeling/ldm_pdm_code.png?raw=true" alt="data modeling ldm, pdm" width="600">
</a> -->

## Data models abstractions

The table shows the different data models abstractions and their content. We can see that conceptual is an overview suitable for business, logical may also be suitable for business, while physical is more technical and implementation ready.

|                                  | Conceptual | Logical | Physical |
| -------------------------------- | ---------- | ------- | -------- |
| Relationship Labels              | x          |         |          |
| Entity Names                     |            | x       |          |
| High-level Relationships         | x          | x       | x        |
| Cardinality of Relationships     | x          | x       | x        |
| Optionality of Relationships     | x          | x       | x        |
| Attributes                       |            | x       |          |
| Attribute Preliminary Data       |            | x       |          |
| Primary keys                     |            | x       | x        |
| Foreign keys                     |            | x       | x        |
| Table Names                      |            |         | x        |
| Column Names                     |            |         | x        |
| Column Data Types (DB‑specific)  |            |         | x        |
| Column Constraints (DB‑specific) |            |         | x        |

## Database modeling language (dbml)

Install [DBML extensions in vscode by Juste Bocovo](https://marketplace.visualstudio.com/items?itemName=bocovo.dbml-erd-visualizer) so that you can save your data models and store them in source control. It will give a settings.json in .vscode in your repo, add .vscode to .gitignore as this setting is only for you and not to share with others.

However we'll be using [dbdiagram](https://dbdiagram.io/home) which is easy to get started online. It is good for getting started and has some neat features for auto-completion and syntax highlighting which we don't have in vscode.

> [!NOTE]
> the diagrams are public when using the free version, which is okay for learning but if you are in a company setting, consider either buying it or use local development in vscode and source control with github

## Other videos 📹

- [Data models. Conceptual Vs logical - Learning with me (2022)](https://www.youtube.com/watch?v=rzKMT5qqbQY)
- [How to read Logical Data Models - Ellie.ai - J. Korpela (2024)](https://www.youtube.com/watch?v=zqUqjECv5nM)

## Read more 👓

- [Conceptual vs logical vs physical data models - S. Rivera (2023), ThoughtSpot](https://www.thoughtspot.com/data-trends/data-modeling/conceptual-vs-logical-vs-physical-data-models)
