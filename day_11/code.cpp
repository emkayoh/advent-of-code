#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <cmath>
#include <algorithm>

// Function to split a string by spaces
std::vector<std::string> split(const std::string& str) {
    std::istringstream iss(str);
    std::vector<std::string> tokens;
    std::string token;
    while (iss >> token) {
        tokens.push_back(token);
    }
    return tokens;
}

// Function to trim whitespace from a string
std::string trim(const std::string& str) {
    size_t start = str.find_first_not_of(' ');
    size_t end = str.find_last_not_of(' ');
    return (start == std::string::npos) ? "" : str.substr(start, end - start + 1);
}

// Function equivalent to ext_stone in R
std::string ext_stone(const std::string& stone) {
    if (stone == "0") {
        return "1 ";
    }
    long long stone_num = std::stoll(stone);
    int len = static_cast<int>(std::log10(stone_num)) + 1;
    
    if (len % 2 == 0) {
        long long ee = static_cast<long long>(std::pow(10, len / 2));
        long long ls = stone_num / ee;
        long long rs = stone_num % ee;
        return std::to_string(ls) + " " + std::to_string(rs) + " ";
    }
    return std::to_string(stone_num * 2024) + " ";
}

// Function equivalent to blink in R
std::string blink(const std::string& init) {
    std::vector<std::string> initTokens = split(init);
    std::ostringstream out;

    for (const auto& token : initTokens) {
        out << ext_stone(token);
    }

    return trim(out.str());
}

int main() {
    std::string filename = "input"; // File name equivalent to R's `foi <- 'input'`
    std::ifstream inputFile(filename);

    if (!inputFile.is_open()) {
        std::cerr << "Error: Could not open file " << filename << std::endl;
        return 1;
    }

    // Read the entire file into a string
    std::string tmp;
    std::ostringstream buffer;
    buffer << inputFile.rdbuf();
    tmp = buffer.str();

    // Split the input file content into tokens
    tmp = trim(tmp); // Remove leading and trailing whitespace
    tmp = blink(tmp); // Process the input similarly to the R code

    for (int bb = 1; bb <= 25; ++bb) {
        tmp = blink(tmp);
    }

    // Count the final number of tokens and print it
    size_t count = split(tmp).size();
    std::cout << count << std::endl;

    inputFile.close();
    return 0;
}
