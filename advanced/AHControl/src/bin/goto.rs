use clap::Parser;

use rustypot::servo;
// use rustypot::DynamixelProtocolHandler;
use std::{error::Error, thread, time::Duration};

#[derive(Parser, Debug)]
#[command(author, version, about, long_about = None)]
struct Args {
    /// Serialport
    #[arg(short, long, default_value = "/dev/ttyACM0")]
    serialport: String,
    /// baudrate
    #[arg(short, long, default_value_t = 1_000_000)]
    baudrate: u32,
    /// id
    #[arg(short, long, default_value_t = 1)]
    id: u8,
    /// pos
    #[arg(short, long, default_value_t = 0.0)]
    pos: f64,
}

fn main() -> Result<(), Box<dyn Error>> {
    let args = Args::parse();
    let serialport: String = args.serialport;
    let baudrate: u32 = args.baudrate;
    let id: u8 = args.id;
    let pos: f64 = args.pos;

    println!("正在打开端口 {serialport} 于波特率 {baudrate}");
    println!("移动电机 ({id}) 到指定位置: {pos}");

    let serial_port = serialport::new(serialport, baudrate)
        .timeout(Duration::from_millis(10))
        .open()?;

    // let dph=DynamixelProtocolHandler::v1();
    let mut controller = servo::feetech::scs0009::Scs0009Controller::new()
        .with_protocol_v1()
        .with_serial_port(serial_port);

    let curpos = controller.read_present_position(id)?;
    println!("当前位置: {:?}", curpos);
    controller.write_torque_enable(id, 1)?;
    thread::sleep(Duration::from_millis(1000));
    controller.write_goal_position(id, pos)?;
    thread::sleep(Duration::from_millis(1000));
    println!("退出程序");
    Ok(())
}
