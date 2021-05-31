ref : https://www.youtube.com/watch?v=Yw4rkaTc0f8&t=135s

https://developers.google.com/protocol-buffers/docs/reference/python-generated


To execute: Example of streaming server using grpc and node js for todo application
1)  node server.js 
2)
node client.js abcd
Server done!
Received from server{}
Received from server{"id":1,"text":"abcd"}

3)
node client.js abcdef
Received from server{"id":1,"text":"abcd"}
Server done!
Received from server{"items":[{"id":1,"text":"abcd"}]}
Received from server{"id":2,"text":"abcdef"}
