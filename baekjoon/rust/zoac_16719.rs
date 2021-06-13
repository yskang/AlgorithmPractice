use std::io::{stdin, stdout, BufRead, BufReader, BufWriter, Write};

fn print_word(word: &Vec<String>, show: &mut Vec<bool>) {
    let mut ans: Vec<String> = Vec::new();
    for i in 0..word.len() {
        if show[i] {
            ans.push(word[i].to_string());
        }
    }
    let mut writer = BufWriter::new(stdout());
    writeln!(writer, "{}", ans.join("")).unwrap();
    writer.flush().unwrap();
}

fn find_minimum_letter(word: &Vec<String>, left: usize, right: usize, show_index: &mut Vec<bool>) {
    if left == right {
        return;
    }

    let word_iter = word[left..right].iter();
    let mut zipped_word = word_iter
        .zip((0..word.len()).collect::<Vec<_>>())
        .collect::<Vec<_>>();
    zipped_word.sort_by_key(|v| v.0);

    let index = zipped_word[0].1;
    show_index[index + left] = true;
    print_word(word, show_index);

    find_minimum_letter(word, left + index + 1, right, show_index);
    find_minimum_letter(word, left, left + index, show_index);
}

fn solution(word: Vec<String>) {
    let mut show_index = vec![false; word.len()];
    find_minimum_letter(&word, 0, word.len(), &mut show_index);
}

fn main() {
    let mut reader = BufReader::new(stdin());
    let mut buffer = String::new();

    reader.read_line(&mut buffer).unwrap();
    let word = buffer
        .trim()
        .as_bytes()
        .iter()
        .map(|x| (*x as char).to_string())
        .collect::<Vec<_>>();
    solution(word);
}
