#include <iostream>

class Node {
private:
  short int data;
  short int next;
public:
  Node(short int d, short int n);
  ~Node();
};
Node::Node(short int d, short int n) {
  data = d;
  next = n;
};
Node:: ~Node() { std::cout << "Node Deleted"; };

class LinkedList {
private:
  int head;
public:
  LinkedList(int h) {head = h;};
  ~LinkedList() { std::cout << "List Deleted"; };
  
  //methods for linked list operations
  void insert_at_beginning(int data);
  void insert_at_end(int data);
  void insert_values()
  void display_list();

};

int main() {
  return 0;
}