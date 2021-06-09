import React, { useCallback, useEffect, useMemo, useState } from 'react';
import { Layout, Table } from 'antd';
import { HeaderCustom } from '../../components/Header';
import { ColumnsType } from 'antd/lib/table';
import { Course, Module } from '../../types/course';
import { InfoBlock, PageHeaderText, StyledContent, StyledPageHeader } from './styles';
import { getCourse, getCourses } from "../../api";
import { getCurrentCourse } from "../../utils";
import { Link, useParams } from "react-router-dom";

export const ModulesList = (): JSX.Element => {
  const [loading, setLoading] = useState<boolean>(false);
  const [data, setData] = useState<Module[]>([]);
  useEffect(() => {
    async function getData() {
      setLoading(true);
      await setTimeout(() => {
        setData(getCurrentCourse()?.modules ?? []);
        setLoading(false);
      }, 500);
    }

    getData();
  }, []);
  const columns = useMemo(
    () =>
      [
        {
          title: 'Название',
          dataIndex: 'title',
          width: '20%',
          render: function renderName(value, record) {
            return (
              <p>
                {record.title}
              </p>
            );
          },
          sorter: (a, b) => a.title.localeCompare(b.title),
        },
        {
          title: 'Уроки',
          dataIndex: 'lessons',
          render: function renderLessons(value, record) {
            return (
              <p>
                {record?.lessons.map(lesson =>
                  <Link to={'/lesson/' + lesson.id + '/'}>
                  {lesson.title}
                    <br/>
                </Link>)}
              </p>
            );
          },
          // sorter: (a, b) => a?.modules?.name?.localeCompare(b.teacher.name),
        },
        // {
        //   title: '',
        //   dataIndex: 'join',
        //   render: function renderJoin(value, record) {
        //     return (
        //       <Link to={'course/'+record.id+'/'}>
        //         Подробнее
        //       </Link>);
        //   },
        // },
      ] as ColumnsType<Module>,
    [],
  );
  return (
    <>
      <StyledPageHeader title={<PageHeaderText>Модули</PageHeaderText>} backIcon={false} />
      <InfoBlock>
        <Table<Module>
          columns={columns}
          dataSource={data}
          loading={loading}
          pagination={{ pageSize: 7 }}
        />
      </InfoBlock>
    </>
  );
};
