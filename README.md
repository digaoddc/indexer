# CSS Indexer

Automatically index the important sections of your CSS.

## How to Use

Just...

    index.py $FILE_NAME

`example.scss`

    // == GENERAL
    body { background:#FFF; }

    // == TYPOGRAPHY
    p { color:#000; }

    // == AND SO ON...

Will have this fancy header: 

    /**
      * ========= TABLE OF CONTENTS =========
      * 
      * 01. GENERAL
      * 02. TYPOGRAPHY
      * 03. AND SO ON...
      *
      */ 
     


Ideas? Fixes? Feel free to contribute!
