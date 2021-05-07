import React, { useCallback } from 'react';
import { Button, Form, Input, Switch } from 'antd';
import { register } from '../../api';

export const Registration = (): JSX.Element => {

  const handleFinish = useCallback((values) => {
    register(values);
  }, []);

  return (
    <Form onFinish={handleFinish}>
      <Form.Item
        label='Name'
        name='name'
        rules={[{ required: true, message: 'Please, enter your name!' }]}
      >
        <Input />
      </Form.Item>

      <Form.Item
        label='Email'
        name='email'
        rules={[{ required: true, message: 'Please, enter your email!' }]}
      >
        <Input />
      </Form.Item>

      <Form.Item
        label='Password'
        name='password'
        rules={[{ required: true, message: 'Please, enter your password!' }]}
      >
        <Input.Password />
      </Form.Item>

      <Form.Item
        label='Password repeat'
        name='re_password'
        rules={[{ required: true, message: 'Please, repeat your password!' }]}
      >
        <Input.Password />

      </Form.Item>
      <Form.Item
        label='Are you a student?'
        name='is_student'
        rules={[{ required: true, message: 'Are you a student?' }]}
      >
        <Switch checkedChildren="yes" unCheckedChildren="no" defaultChecked />

      </Form.Item>

      <Form.Item>
        <Button type='primary' htmlType='submit'>
          Submit
        </Button>
      </Form.Item>
    </Form>
  );
};
