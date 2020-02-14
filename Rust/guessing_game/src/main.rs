use std::io; 
use std::cmp::Ordering; 
use rand::Rng;

fn main() {
    println!("Guess the number!");
    let secret = rand::thread_rng().gen_range(1,101);
    let outcome = String::new();


    loop {
        println!("Please Input your guess.");
        let mut guess = String::new();
            io::stdin().read_line(&mut guess)
                .expect("Failed to read line");

        let guess: u32 = guess.trim().parse()
            .expect("Please type a number!");

        match guess.cmp(&secret) {
    	   Ordering::Less => let outcome = String::from("Too Small!"),
    	   Ordering::Greater => let outcome = String::from("Too Big!"),
    	   Ordering::Equal => {
    	       println!("You win!"); 
    	       break;
    	   }
        }

                    println!("{}", x);


        
    }

}
