use image::png::PNGEncoder;
use image::ColorType;
use num::Complex;
use std::fs::File;

fn main() {
    match mandelbrot(
        Complex { re: -2.0, im: -1.0 },
        Complex { re: 3.0, im: 2.0 },
        500.0,
    ) {
        Ok(_) => println!("Done!"),
        Err(msg) => println!("Error: {}", msg),
    };
}

fn escape_time(c: Complex<f64>, limit: u32) -> u32 {
    let mut z: Complex<f64> = Complex { re: 0.0, im: 0.0 };
    for i in 0..limit {
        z = z * z + c;
        if z.norm_sqr() > 4.0 {
            return i;
        }
    }
    limit
}

fn mandelbrot(
    z_offset: Complex<f64>,
    z_range: Complex<f64>,
    res: f64,
) -> Result<(), std::io::Error> {
    let width: usize = (res * z_range.re) as usize;
    let height: usize = (res * z_range.im) as usize;
    let mut matrix: Vec<u8> = vec![0; width * height * 3];
    for row in 0..height {
        for col in 0..width {
            let c = z_offset
                + Complex {
                    re: ((col as f64) / res),
                    im: ((row as f64) / res),
                };
            matrix[3 * col + 0 + (width * 3) * row] = (escape_time(c, 100) * 2) as u8;
            matrix[3 * col + 1 + (width * 3) * row] = (escape_time(c, 100) as f64 * 1.8) as u8;
            matrix[3 * col + 2 + (width * 3) * row] = (escape_time(c, 100) as f64 * 1.5) as u8;
        }
    }

    let output = File::create("mandelbrot.png")?;
    let encoder = PNGEncoder::new(output);
    encoder.encode(&matrix, width as u32, height as u32, ColorType::RGB(8))?;
    Ok(())
}
