1. Difference between char and varchar
   1. Char is fixed length and varchar is variable length
   2. var char add upto 2 byte(depend if the length of char is bigger than 255) to variable to sotre its length
   
2. Difference between clustered index and non-clustered index
   1. Clustered Index: means the order of the data have the same corrsponding order realation with its index(key value)
   2. non-cluster index: means the data and its index are not corrsponded. Each index contain its key value.
   3. Cluster index have fast speed and less memory than non-cluster
   4. A clustered index is used to define the order or to sort the table or arrange the data by alphabetical order just like a dictionary.
   5. A non-clustered index collects the data at one place and records at another place.
   6. Cluster index can store data on the disk with non-cluster index cant
   
3. Difference between normal table and temporary table
   1. Two types of temporary table
      1. Internal temporary table
         1. information_schema temporary table
         2. The other type is that when the session executes the query, if the execution plan contains "Using temporary", a temporary table will be generated.
      2. Normal table is just regular table in sql, so every time you use the normal table it wil cause you logging in your database, consume space, and require log flush on every commit.
      3. If it is temporary data, you should use temporary table
      4. The main difference between a temporary table and a normal table is whether the data is automatically cleaned up after the instance, session, or statement ends
      5. Temporary tables in different sessions can have the same name.


4. If you declare variable outside function in JS can you use it
   1. Variables declared outside of any function become global variables. Global variables can be accessed and modified from any function.
   2.  variable with 'var' are local variable which without 'var' are global variable
   
5. What is error code 150 means in sql
   1. A transition table was named in an INSERT, UPDATE, DELETE, MERGE, or TRUNCATE statement in a triggered action. Transition tables are read-only.
   2. The view named in the INSERT, UPDATE, DELETE, MERGE, or TRUNCATE statement is defined in such a way that the requested insert, update, delete, or truncate operation cannot be performed upon it.
   
   
6. What's the difference between delete from and truncate difference
   1. DELETE is a DML(Data Manipulation Language) command and is used when we specify the row(tuple) that we want to remove or delete from the table or relation. The DELETE command can contain a WHERE clause. If the WHERE clause is used with the DELETE command then it removes or deletes only those rows(tuple) that satisfy the condition otherwise by default it removes all the tuples(rows) from the table.  Remember that DELETE logs the row deletions.
   2. TRUNCATE is a DDL(Data Definition Language) command and is used to delete all the rows or tuples from a table. Unlike the DELETE command, the TRUNCATE command does not contain a WHERE clause. In the TRUNCATE command, the transaction log for each deleted data page is not recorded. Unlike the DELETE command, the TRUNCATE command is fast. We cannot roll back the data after using the TRUNCATE command. 
   
7. Difference between "==" and "==="
   1. ‘==’ compare the value of variable.
   2. '===' compare the data type of variables.
   
8.  Difference between inner and left join
    1.  Inner join match the value in both table
    2.  left join match the value from the left table first then match it with right table