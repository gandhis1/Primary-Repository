#include <iostream>
#include <memory>
#include <initializer_list>
#include <exception>
#include <random>
#include <algorithm>

template<typename T>
class Node {
    public:
        std::shared_ptr<Node<T>> next = nullptr;
        T data;
};

template <typename T>
class Stack {
    public:
        Stack() {}
        Stack(std::initializer_list<T> init) {
            first_node = std::make_shared<Node<T>>();
            auto current = first_node;
            for (auto& val: init) {
                current->data = val;
                current->next = std::make_shared<Node<T>>();
                current = current->next;
            }
        }
        operator[](int&& index) {
            auto current_node = first_node;
            for (int i = 1; i < index; ++i) {
                current_node = current_node->next;
                if (current_node == nullptr)
                {
                    auto err_msg = "The index specified is out of bounds.";
                    throw std::out_of_range(err_msg);
                }
            }
            return current_node->data;
        }
        T pop()
        {
            auto return_node = first_node;
            first_node = first_node->next;
            return first_node->data;            
        }
        void push(T&& value)
        {
            auto previous_first_node = first_node;
            first_node = std::make_shared<Node<T>>();
            first_node->data = value;
            first_node->next = previous_first_node;
        }
        int length()
        {
            auto current_node = first_node;
            int i = 1;
            while (current_node->next != nullptr)
            {
                ++i;
                current_node = current_node->next;
            }
            return i;
        }

    private:
        std::shared_ptr<Node<T>> first_node = nullptr;

};

int main() {
    // Generate random numbers
    std::mt19937 gen(999);
    std::uniform_real_distribution<double> dist(0.0, 100000.0);

    Stack<int> seq;
    for (int i = 0; i < 1000000; ++i){
        seq.push(dist(gen));
    }

    std::cout << "The length of the stack is: " << seq.length() << std::endl;
}