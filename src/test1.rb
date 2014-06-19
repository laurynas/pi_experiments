#!/usr/bin/ruby

require 'pi_piper'
include PiPiper

led1 = Pin.new(pin: 22, direction: :out)
led2 = Pin.new(pin: 21, direction: :out)
relay1 = Pin.new(pin: 24, direction: :out)

watch pin: 17 do
  puts "Pin 17 changed from #{last_value} to #{value}"
  led1.update_value(value)
  #relay1.update_value(value)
end

watch pin: 23 do
  puts "Pin 23 changed from #{last_value} to #{value}"
  led2.update_value(value)
end

PiPiper.wait
