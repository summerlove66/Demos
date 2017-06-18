package hui.test.learn;

import java.io.IOException;
import java.util.concurrent.TimeoutException;

import com.rabbitmq.client.Channel;
import com.rabbitmq.client.Connection;
import com.rabbitmq.client.ConnectionFactory;

public class Product {
	public final static String QUEUE_NAME = "rabbitMQ.test";
	public static Connection connection;
	public static void main(String[] args) throws IOException, TimeoutException {
		
		new Product().sendMessage("我爱你");
		
	}
	public  Channel getChannl() throws IOException, TimeoutException{
		ConnectionFactory factory = new ConnectionFactory();
		factory.setHost("localhost");
		factory.setUsername("hui");
		factory.setPassword("smile");
		connection = factory.newConnection();
		Channel channel = connection.createChannel();
		channel.queueDeclare(QUEUE_NAME, false, false, false, null);
		return channel;
	
	}
	
	public void sendMessage(String message) throws IOException, TimeoutException{
		Channel channel = getChannl();
		channel.basicPublish("", QUEUE_NAME, null, message.getBytes("UTF-8"));
		System.out.println("生产了一个消息：" + message);
		channel.close();
		connection.close();
		
	}
	
	
}
