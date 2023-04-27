class Node { // Singly linked list node class
    constructor(val) {
        this.value = val; // Holds value for this node 
        this.next = null; // Pointer to next node
    }
}

class SLList { //The singly linked list class itself
    constructor() { //Will start with no nodes
        this.head =null; //Head points to the first node
    }
}

// Write a method to return the value(not the node) at the head of the list.If the list is empty, return null.

function front(list){
    if (list === null) {
        return null;
    }
    return list.value;
}
list = {
    value: 2,
    next: {
        value: 12,
        next: null
    }
}
head = front(list);
console.log(head)


// Remove Front
// Write a method to remove the head node and return the new list head node.If the list is empty, return null.

function remove_front(list) {
    if (list === null) {
        return null;
    }
    return list.next;
}
list = {
    value: 27,
    next: {
        value: 22,
        next: null
    }
}


// Add Front
// Write a method that accepts a value and create a new node, assign it to the list head, and return a pointer to the new head node.

function add_front(list, val){
    new_node = {
        val: val,
        next: list
    }
    return new_node;
}

linked_list = {
    value: 17,
    next: {
        value: 9,
        next: {
            value: 2,
            next: null
        }
    }
}

console.log(add_front(linked_list, 12))

// Bonus
// Add to Back
// Write a method that accepts a value and create a new node, assign it to the end of the list

function add_back(list, value){
    newNode = {
        value : value,
        next : null
    };
    if (list === null) {
        return newNode;
    }
    currentNode = list;
    while (currentNode.next !== null) {
        currentNode = currentNode.next;
    }
    currentNode.next = newNode;
    return list
}
linked_list = {
    value: 17,
    next: {
        value: 9,
        next: {
            value: 2,
            next: null
        }
    }
}

console.log(add_back(linked_list, 20))