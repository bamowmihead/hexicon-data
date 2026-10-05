# questions/ — written by Claude's weekly pass only

The channel from Claude back to Reece. Step ② of the Brain v3 contract;
**nothing is written here yet.**

* **Writer:** the weekly pass. It will write `inbound.json`: new questions for
  the questions table in Hexicon, plus an `ingested` list of the resolved
  question ids it has already read.
* **Reader:** Hexicon, which ingests `inbound.json` into its questions table and
  stamps the resolved rows it names.
* **Hexicon never writes here.**
